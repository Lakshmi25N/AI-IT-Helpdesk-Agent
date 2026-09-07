from datetime import datetime


def network_diagnostic(connection_type: str, internet_status: str) -> str:
    """
    Diagnose a basic network connectivity situation.

    Args:
        connection_type: Type of connection, such as WiFi or Ethernet.
        internet_status: Current internet status.

    Returns:
        A diagnostic message.
    """

    connection = connection_type.lower()
    status = internet_status.lower()

    if connection == "wifi" and status in [
        "not working",
        "no internet",
        "disconnected"
    ]:
        return (
            "Diagnostic result: The device appears to have a Wi-Fi "
            "connection but internet connectivity is unavailable. "
            "Possible causes include router connectivity, DNS, "
            "network configuration, or network adapter problems."
        )

    if connection == "ethernet" and status in [
        "not working",
        "no internet",
        "disconnected"
    ]:
        return (
            "Diagnostic result: Ethernet connection may be unavailable. "
            "Check the network cable, network adapter, and network connection."
        )

    return (
        "Diagnostic result: No obvious connectivity problem was "
        "identified from the provided information."
    )

from langchain_core.tools import tool


@tool
def diagnose_network(connection_type: str, internet_status: str) -> str:
    """
    Diagnose a basic Wi-Fi or Ethernet connectivity problem.
    """

    return network_diagnostic(
        connection_type,
        internet_status
    )