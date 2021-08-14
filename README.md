# ngflask
Serving static files and directories from your local machine over the Internet with just one command.

The script first binds a flask server to the given address and starts sharing files from the specified directory.

It then creates a tunnel through the Ngrok network and prints the public URL pointing to the local flask server.

## Installation

```bash
sudo apt install python3 python3-pip
git clone https://github.com/derstolz/ngflask
cd ngflask
pip3 install -r requirements.txt
sudo link flask-ngrok.py /usr/bin/ngflask
```
## Usage

### Serve files and folder from the current working directory
`ngflask`

### Serve files and folders from the /tmp directory
`ngflask --directory /tmp`

### Bind the server to a specific address
`ngflask --ip 10.10.10.10 --port 5050`

### Print the banner
`ngflask -h`
