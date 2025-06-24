from smartcard.System import readers

reader_list = readers()
if not reader_list:
    print("❌ কোনো রিডার পাওয়া যায়নি!")
    exit()

reader = reader_list[0]
connection = reader.createConnection()
connection.connect()

GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
data, sw1, sw2 = connection.transmit(GET_UID)

if sw1 == 0x90 and sw2 == 0x00:
    uid = ''.join(['%02X' % byte for byte in data])
    print("✅ কার্ড UID:", uid)
else:
    print("❌ কার্ড UID পড়া যায়নি!")
