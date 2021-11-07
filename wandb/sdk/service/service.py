"""grpc service.

Reliably launch and connect to grpc process.
"""

import os
import subprocess
import sys
import tempfile
import time
from typing import Any, Dict, Optional

from . import port_file
from .service_base import ServiceInterface
from .service_sock import ServiceSockInterface

# from .service_grpc import ServiceGrpcInterface


class _Service:
    _use_socket: bool
    _grpc_port: Optional[int]
    _sock_port: Optional[int]
    _service_interface: ServiceInterface

    def __init__(self) -> None:
        self._stub = None
        self._use_socket = False
        self._grpc_port = None
        self._sock_port = None
        self._service_interface = ServiceSockInterface()

    def _wait_for_ports(self, fname: str, proc: subprocess.Popen = None) -> bool:
        time_max = time.time() + 30
        while time.time() < time_max:
            if proc and proc.poll():
                # process finished
                print("proc exited with", proc.returncode)
                return False
            if not os.path.isfile(fname):
                time.sleep(0.2)
                continue
            try:
                pf = port_file.PortFile()
                pf.read(fname)
                if not pf.is_valid:
                    time.sleep(0.2)
                    continue
                self._grpc_port = pf.grpc_port
                self._sock_port = pf.sock_port
            except Exception as e:
                print("Error:", e)
            return False
        return False

    def _launch_server(self) -> None:
        """Launch server and set ports."""

        # References for starting processes
        # - https://github.com/wandb/client/blob/archive/old-cli/wandb/__init__.py
        # - https://stackoverflow.com/questions/1196074/how-to-start-a-background-process-in-python

        kwargs: Dict[str, Any] = dict(close_fds=True)

        pid = os.getpid()

        with tempfile.TemporaryDirectory() as tmpdir:
            fname = os.path.join(tmpdir, f"port-{pid}.txt")

            pid_str = str(os.getpid())
            exec_cmd_list = [sys.executable, "-m"]
            # Add coverage collection if needed
            if os.environ.get("COVERAGE_RCFILE"):
                exec_cmd_list += ["coverage", "run", "-m"]
            service_args = [
                "wandb",
                "service",
                "--port-filename",
                fname,
                "--pid",
                pid_str,
                "--debug",
            ]
            service_args.append("--serve-sock")
            service_args.append("--serve-grpc")
            internal_proc = subprocess.Popen(
                exec_cmd_list + service_args, env=os.environ, **kwargs,
            )
            self._wait_for_ports(fname, proc=internal_proc)

    def start(self) -> None:
        self._use_socket = True
        self._launch_server()

    @property
    def use_socket(self):
        return self._use_socket

    @property
    def grpc_port(self) -> Optional[int]:
        return self._grpc_port

    @property
    def sock_port(self) -> Optional[int]:
        return self._sock_port

    @property
    def service_interface(self) -> ServiceInterface:
        return self._service_interface
