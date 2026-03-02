import re


def step_saved_host(ctx, host, port):
    ctx.setdefault("hosts", []).append({"host": host, "port": port})


def step_on_connection_list(ctx):
    ctx["screen"] = "connection_list"


def step_select_host(ctx):
    ctx["selected_host"] = ctx.get("hosts", [{}])[-1]


def step_attempt_connection(ctx, target):
    ctx["connection_target"] = target
    ctx["status"] = "connecting"


def step_status_becomes(ctx, status):
    ctx["status"] = status


def step_active_session(ctx, target):
    ctx["active_session"] = target
    ctx["status"] = "connected"


def step_disconnect(ctx):
    ctx["active_session"] = None


def step_session_ends(ctx):
    ctx["status"] = "disconnected"


def step_open_credentials(ctx):
    ctx["screen"] = "credentials"


def step_enter_credentials(ctx, username, password):
    ctx["credentials"] = {"username": username, "password": password}


def step_submit_credentials(ctx):
    ctx["submitted"] = True


def step_auth_result(ctx, result):
    ctx["auth_result"] = result


def step_error_message(ctx, message):
    ctx["last_error"] = message


def step_open_settings(ctx):
    ctx["screen"] = "settings"


def step_enable_view_only(ctx, setting_label):
    ctx.setdefault("settings", {})["view-only"] = "enabled"


def step_setting_stored(ctx, key, value):
    ctx.setdefault("settings", {})[key] = value


def step_next_connection_mode(ctx, mode):
    ctx["next_mode"] = mode


def step_select_color_depth(ctx, depth):
    ctx.setdefault("settings", {})["color-depth"] = depth


def step_next_connection_requests(ctx, depth):
    ctx["next_depth"] = depth


STEP_DEFINITIONS = [
    (re.compile(r'^a saved VNC host "(.+)" on port "(\d+)"$'), step_saved_host),
    (re.compile(r'^the demo app is on the connection list$'), lambda ctx: step_on_connection_list(ctx)),
    (re.compile(r'^the user selects the host entry$'), lambda ctx: step_select_host(ctx)),
    (re.compile(r'^the app attempts a VNC connection to "(.+)"$'), step_attempt_connection),
    (re.compile(r'^the connection status becomes "(.+)"$'), step_status_becomes),
    (re.compile(r'^the status transitions to "(.+)"$'), step_status_becomes),
    (re.compile(r'^an active VNC session to "(.+)"$'), step_active_session),
    (re.compile(r'^the user taps "Disconnect"$'), lambda ctx: step_disconnect(ctx)),
    (re.compile(r'^the session ends cleanly$'), lambda ctx: step_session_ends(ctx)),
    (re.compile(r'^the status becomes "(.+)"$'), step_status_becomes),
    (re.compile(r'^the user opens the credentials prompt$'), lambda ctx: step_open_credentials(ctx)),
    (re.compile(r'^the user enters username "(.+)" and password "(.+)"$'), step_enter_credentials),
    (re.compile(r'^the app submits credentials to the VNC server$'), lambda ctx: step_submit_credentials(ctx)),
    (re.compile(r'^the authentication result is "(.+)"$'), step_auth_result),
    (re.compile(r'^an error message "(.+)" is shown$'), step_error_message),
    (re.compile(r'^a VNC session settings screen is open$'), lambda ctx: step_open_settings(ctx)),
    (re.compile(r'^the user enables "(.+)"$'), step_enable_view_only),
    (re.compile(r'^the setting "(.+)" is stored as "(.+)"$'), step_setting_stored),
    (re.compile(r'^the next connection runs in "(.+)" mode$'), step_next_connection_mode),
    (re.compile(r'^the user selects color depth "(.+)"$'), step_select_color_depth),
    (re.compile(r'^the next connection requests "(.+)" pixels$'), step_next_connection_requests),
]
