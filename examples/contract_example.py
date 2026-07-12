from ice.system import System, LocalSystem
from ice.contract import Contract

def assemble_contract():

    # Simulate true evaluation as if checks were built from API
    def cap_check_a(target):
        # Do something with target.connect()
        return True
    def cap_check_b(target):
        # Do something with target.connect()
        return False

    # Define systems
    system_a = System("proxmox", "root", "password")
    system_b = System("heartbeat_vm", "root", "password")
    system_lcl = LocalSystem("local")

    # Define contract
    contract = Contract(
        src=system_b,
        dst=system_a,
        lcl=system_lcl,
        expression=lambda src, dst, lcl: cap_check_a(dst) or cap_check_b(src)
    )

    # Evaluate dummy contract
    print(contract.evaluate())

if __name__ == "__main__":
    test()