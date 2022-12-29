import utils
import action


class CreateLinstor(object):
    def __init__(self):
        self.drbd_cmd = action.Drbd()
        self.linstor_cmd = action.Linstor()

    def check_software(self, ssh_conn):
        drbd_result = self.drbd_cmd.drbdadm_version(ssh_conn)
        self.linstor_cmd.start_server(ssh_conn)
        server_result = self.lintsor_cmd.check_server(ssh_conn)
        client_result = self.lintsor_cmd.check_client(ssh_conn)

        return drbd_result, server_result, client_result




