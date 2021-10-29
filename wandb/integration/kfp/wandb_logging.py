def wandb_log(
    func=None,
    # /,  # py38 only
    settings=None,
    WANDB_APP_URL=None,
    WANDB_API_KEY=None,
    WANDB_BASE_URL=None,
):
    """Wrap a standard python function and log to W&B
    """
    from functools import wraps
    import os
    import wandb

    def coalesce(*arg):
        return next((a for a in arg if a is not None), None)

    settings = coalesce(settings, wandb.Settings())
    WANDB_APP_URL = coalesce(WANDB_APP_URL, os.getenv("WANDB_APP_URL"))
    WANDB_API_KEY = coalesce(WANDB_API_KEY, os.getenv("WANDB_API_KEY"))
    WANDB_BASE_URL = coalesce(WANDB_BASE_URL, os.getenv("WANDB_BASE_URL"))

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            os.environ["WANDB_APP_URL"] = WANDB_APP_URL
            os.environ["WANDB_API_KEY"] = WANDB_API_KEY
            wandb.login(host=WANDB_BASE_URL)

            with wandb.init(settings=settings) as run:
                result = func(*args, **kwargs)
                run.log({f"{func.__name__}_result": result})
                return result

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)
