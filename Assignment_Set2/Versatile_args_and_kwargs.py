def log_event(message, *args, **kwargs):
    print("Event:", message)
    print("Details:", args)
    print("Metadata:", kwargs)

log_event(
    "User Login",
    "admin",
    "dashboard",
    timestamp="10:00 AM",
    status="Success"
)