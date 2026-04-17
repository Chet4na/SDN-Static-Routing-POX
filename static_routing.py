from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch %s connected", event.connection)

def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port

    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port

    # STATIC ROUTING LOGIC
    if in_port == 1:
        return #drop packets
    elif in_port == 2:
        msg.actions.append(of.ofp_action_output(port=1))

    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

