def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
 banh_dau_xanh = {"đường":0.04,"đậu":0.07}
 banh_thap_cam = {"đường":0.06,"đậu":0}
 banh_deo = {"đường":0.05,"đậu":0.02}
 nguyen_lieu ={}
 duong_hop_banh = sl_bdx*banh_dau_xanh["đường"] + sl_btc*banh_thap_cam["đường"] + sl_bd*banh_deo["đường"]
 dau_hop_banh = sl_bdx*banh_dau_xanh["đậu"] + sl_btc*banh_thap_cam["đậu"] + sl_bd*banh_deo["đậu"]
 nguyen_lieu["đường"] = duong_hop_banh
 nguyen_lieu["đậu"] = dau_hop_banh

    