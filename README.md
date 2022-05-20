# pezos
Blockchain course project.
- [x] P2P connections.
- [x] Block validators (hash, timestamp, context, operations, signatures).
- [x] Operation injections.
- [x] Miner (validation deamon).
- [x] Signing utilities (ed25519 & blake2)
- [x] Interactive loop (demo).
- [x] Block & context pretty printers.

## Installation
`pip3 install -r requirements.txt`

## Deployment 
put the public_key and secret_key in the following file:  
`src/utility/keys`

To run the software please type at the root of the folder:

`python3 src/main.py`

To run it into dev mode and interact with the software, you can use the option demo:

`python3 src/main.py demo`

Follow the instruction on the screen to interact with the block.
