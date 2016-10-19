from btle import Peripheral, ADDR_TYPE_RANDOM, AssignedNumbers

class HRM(Peripheral):
    def __init__(self, addr):
        Peripheral.__init__(self, addr)

if __name__=="__main__":
    cccid = AssignedNumbers.client_characteristic_configuration
    hrmid = AssignedNumbers.heart_rate
    hrmmid = AssignedNumbers.heart_rate_measurement

    hrm = None
    try:
        hrm = HRM('0c:8c:dc:07:c1:e5')

        service, = [s for s in hrm.getServices() if s.uuid==hrmid]
        ccc, = service.getCharacteristics(forUUID=str(hrmmid))

        if 0: # This doesn't work
            ccc.write('\1\0')

        else:
            desc = hrm.getDescriptors(service.hndStart,
                                      service.hndEnd)
            d, = [d for d in desc if d.uuid==cccid]

            hrm.writeCharacteristic(d.handle, '\1\0')

        def print_hr(cHandle, data):
            bpm = ord(data[1])
            print bpm
        hrm.delegate.handleNotification = print_hr

        for x in range(10):
            hrm.waitForNotifications(3.)

    finally:
        if hrm:
            hrm.disconnect()