# data_bridge.py

data_bridge = {
    # Data bridge Arbitrum Sepolia
    "ARB - BASE": '0x56591d59627373700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC0000000000000000000000000000000000000000000000000002713d18f1a0e6e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "ARB - OP SEPOLIA": '0x56591d596f7073700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027145fa28cc803000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "ARB - BLAST": '0x56591d59626c73730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027145fbe6c7600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',

    # Data bridge OP Sepolia
    "OP - BLAST": '0x56591d59626c73730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027145fbdb9da50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "OP - ARB": '0x56591d59617262740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC000000000000000000000000000000000000000000000000000270d8283cee700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "OP - BASE": '0x56591d59627373700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027143a4a846afb000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',

    # Data bridge Blast Sepolia
    "BLAST - OP": '0x56591d596f7073700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004cbb1421df1cf362dc618d887056802d8adb7bc00000000000000000000000000000000000000000000000000027145fa1279ef3000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "BLAST - ARB": '0x56591d59617262740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC000000000000000000000000000000000000000000000000000270dabdd97d700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "BLAST - BASE": '0x56591d59627373700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027145fa0ae6cd5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',

    # Data bridge Base Sepolia
    "BASE - OP": '0x56591d596f7073700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027145fa125558d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "BASE - ARB": '0x56591d59617262740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC000000000000000000000000000000000000000000000000000270dab96114b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',
    "BASE - BLAST": '0x56591d59626c73730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC00000000000000000000000000000000000000000000000000027145fbe6c7600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000027147114878000',


    
}
