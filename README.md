# ngflask
Serving static files and directories over Flask/Ngrok with just one command

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