from coapthon.client.helperclient import HelperClient

client = HelperClient(server=("127.0.0.1", 5671))
response = client.get("hello-world")
print(response.payload)

client = HelperClient(server=("127.0.0.1", 5671))
response = client.get("ping")
print(response.payload)

client.stop()


