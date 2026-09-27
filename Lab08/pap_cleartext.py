# PAP: the password travels as-is. Anything that can read the traffic reads the password.
wire = "USER alice PASS Tr0pical!9"
print("  on the wire:", wire)
print("  -> an eavesdropper read the password 'Tr0pical!9' directly, no cracking needed.")
