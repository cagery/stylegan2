import pretrained_networks

#path = pretrained_networks.get_path_or_url("gdrive:networks/stylegan2-ffhq-config-a.pkl")
G, D, GS = pretrained_networks.load_networks("gdrive:networks/stylegan2-ffhq-config-a.pkl")