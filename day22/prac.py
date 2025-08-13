class TV:
	def power_on(self):
		print("TV is now ON")
class AirConditioner:
	def power_on(self):
		print("Air Conditioner is now ON")
class Speaker:
	def power_on(self):
		print("speaker is now ON")
def remote_control(device):
	device.power_on()
tv=TV()
ac=AirConditioner()
speaker=Speaker()

for device in[tv, ac, speaker]:
	remote_control(device)
	print(id(device))

for obj in[tv, ac, speaker]:
	print(id(obj))
