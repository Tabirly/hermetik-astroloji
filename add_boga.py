import re

links_text = """
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZ339CyLmLYyt1a6sm8ztK-tb_tviE0XRC8ot6JNFBWqk7_3bvxmT6PehorefBW8gr6bJ5MSBHf6ajrba-qmNbhrEu_Wz0HEnjH-Kus-rM5uqFVT2shxdTg1tAgVxAHFfjPBrDlN5Nzzz_J-dIsuD-Z_54jhBg0qt78MqD9guQVMqBHWQy8NrjmDBHNlA/s320/boga-4-yontulmus-tas-uzerine-oturan-boga-nigredo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAUBtu2Frm4BMeU9mdVYdvKjibw_L_gjvXtAaV9tyfpg7_onOttz1NPKRj8afZ6KWmsRkYvBbB0BXsC0S90nNOrlI17-Y6ZlnyACHGNtyHUJCEF4yPoE_tCzdw_2rx-57WbuLHJ-ZJ39epMHX_kwos52iBVGH20ZBWFjZSAiV7nfHVWmf35i-4sJY2cRo/s320/boga-5-zengin-kadin-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0BonrK8d6lC8Z3CiSIFBDYmlr7caBPmZlO7EyHvKR46f7H_Nq9YmCa8z9kH_8MNpxvnOHl3YBKGkRYoxmbMWDa2UkVuFWVzDCJD4-ekOPMKgBPt9bcHFJQyRzDk91ED-fkZk9rmb2d-06eq4aFTysccqPHSIloZaBljIIo5-42WwirGGoOWU7kRA_jX0/s320/boga-6-altin-yildiz-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXvlPxK8o97e2nV5EnDSn4MELWVM4YA7CRsEMk55M31ew3ORfOdEDWOfqyHkYBPArr6fwUslvC-uFbhu7Tj4Av11KiaJHpaZRean0Re2omOEatWl6ylLeLOS2rD_7KZVi585DJBYTMt8c3clgsiwnUKxyT_g9G4M4Ojg84CvYYFgljYD94ykhtlCv6GhA/s320/boga-7-insa-halinde-tapinak-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEib8naS-qJe7YFPgQ-Y7ITGbjouRNV2DLi6gTjn6vsuOgOiKyoMUTnPQUxxrin65GyA23_CT7BO5TPyCdKXeVg_BFjeLpqb2MGxPtzVX7Cc9eZA708mwo3Dkaj8kquWCBMtWzmZmf1j_lxtgdEUPKQeFd2IfssEEqu0TAt4fIZs6W-nzRWMDwTQkqhuyAc/s320/boga-8-gul-bahcesi-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieAreDNxyHWODnCY8_HWArPdl5jB1px5b883EWwLK067VR2AYCe9s7f8pyI5d_OqiYHAnj-6tX5wuHEA3Wd5znR3Fi2uOFBsD6HEwk5H3i2FeMlppsCirAcXRgMXF-96_1-LvvIEZwvzwqTtQTS6A824GjemToj_elMWwEnbBLcH-EtaYWOc70S0_vk2c/s320/boga-9-cift-toprakla-calisiyor-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0rFQfOmZ9GxVbjNOBgMCAmCzOkSukVFHt-YHwfgYWf7MZXV-UaV9L5Q94L4M9_ghtdLY93EvCJuqPrt-FfG3fe_O-Y_t2jodlnthSoSckErIgoa1dkl67xPDZns3FC4ds7d5AZo6WdZBYn-FZT8wfv_ZtKlrR7wPKFulEedvkyfio54O082ZuQNPU7oY/s320/boga-10-coban-surusunu-yonlendiriyor-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8_TJLfNmMpVZjNqGyfBHgYqBMAkurRK9xGIyTpt71D27DWi55rdv78p_L0EZaxGiX6LCIUVf7612HfOQ7mnzQZp46M5mqpttpR0OjgNa9imW1-D_J2hWLReJ_0n1oBU4hkU54Ypt62NLXZ17KAmfjM_br9Gc4FuDIWw2Trkim_yvDCFrLg3XKfZzK3mA/s320/boga-11-sofrada-toplanan-insanlar-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfn_qdZ-_U-sTW38-iMnZsdxyjPy35jx9gsnKNjA9PWF2PxBob7V7C3C6bNOR6seO2yrzT27fea-DNhxwtQQShq9CslO4qqIy8WiaPQ7cX2UdCfj7eNrO4pPp3WtIu84G1iXy1j5CQdM4H2xux-ZuaQcuh0Xbpz7UIo2YRYO0JFP4RoITnOR5rSKZ4HbA/s320/boga-12-parlayan-elmas-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_ir0DosFiHd1vu3NxqcZG2Sx9NWRQ5ajGFmrNpMArw5541beAu-JI8B0u_VCflXgLLkrhn2Ox-YgomNlo41BskktFB2UQd_qcly4dvGllDQZP3eEuJGSqe3ZtzUgzuIzn-F_EGCWbWr7li5sOyk_YKT6t1pz8ezY9DXZTtjY476btqhNZGcz7owQbf90/s320/boga-13-ekin-eken-ciftci-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPz5BVMs1QpPQdzmdyrw8lWYmDunel84r_WzxiAdedh5Zf60PfghnERfPEfLlKMoXnUymfC169JPYSPxKDR9fjIgWqL3wxozzqCFJG4oqHkUAQiPnYxibSEJcZrkC0ggXVPi_RIVfVEvVB_I-Oz_sppS2lHOX8dLeeki8BMKHiP5wRs8moI-zhcOAKMRs/s320/boga-14-cicek-acan-agac-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUtqkzUIZL3fvg-R4DQnwW5zS3VE8lhd-eQxbcww_vjCfiyvOEr0Ob5NgkvzxlW3_KWEdJlmaPOzZH9PuJOICo6r2-T3ald6MdAJbEWOs0gdrb9FK1AZnQvu_STDrIRvTJUtA544bk06_YJ-J8_g0klDomzlz9MREnRyOSSjN8I_kLUcvibT8ASihtjZ0/s320/boga-15-cocuklar-halat-cekiyor-rubedo.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT2-Yxpu_Rymd8D0jhQ33CzATY-vi4-jxz5MQHrSyLKEh2-N9TfntWSfEw-HMd8znRfyOSCLC7nQS51Q34psREIfU98phNd85bZFeYlqb5RCvTLSxC_i5hY9OhEv7kruCMHi-Q6HBfATRaZmH435zmE7jW68TKXo5vSnM3-Qka7TSk2SBOlI2fE7Xb-KA/s320/boga-16-kadin-toprakla-dua-eder-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimb-W3CiDFUjtGBl-8sLoLvCKKgxajs4XfU64XkOUfFzcLdkHAHd0rx8yLNk72BQMe85lyn3tIpDkoHKdlABysQntRiR2EGHYYW6Dh2cbwoVib4R7qcTgT4kOdlSktr4_7UXrAGI2OLlNgWVteXQlszc8chFCrRsLjbIrQYb7WFj04rwnjL4JsHrRHpK0/s320/boga-17-inci-takan-kadin-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgme85Mn4um9_JHGCGCmfcpF4EBQLXRim0-_nld4KiCRINn36MCbjnmjiddKukBtdPMS0DmAx1NUbux9JxxGFQeqvxSht2Z6wsCPIDICxHHChj1HYwzSAIx41YFeIp2UVaeKrcHCGSrKRkbRZYjjd3SnDXpoRry_HeSZS0NUR8Ewj2Xnpbl5PDHH6iYCb0/s320/boga-18-pisen-ekmek-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8t-eli9iXCQ88QrSdIKbEjJfN4Z5R9qAPkE5z_dIdbJ7B3E1ozw9WdMd4Po1p18xYHDMNX28Zxn9ok2XGqV6lV8HMv_-ubOZKHn1avHq0aNwPcDzfNPsXxa8-tAnFAEsbHcpc3PxbSPxFSKSwovIYUpwmEKKLMsLoCY5V49C-NDg2PXixLsBrB5f_0Vc/s320/boga-19-tas-duvar-oruluyor-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLdjbs7zTjTMvAmvY8eI-OmjKNqg1XsKH2KHD8F9DgJ9cConxleY2-o4RBiyJ9Gg4x5n6DduLYo29E6Arjj7unq7hPtNp34M3448bcOy_e6pG6N-3OaG4HIjpVZJic99C9I-UJ6Dfxim2OyWFTFctNAB2OgXyNL96bD6reMH8LiHfUBPJYkXwtgv-UbLA/s320/boga-20-ay-isiginda-parlayan-gol-rubedo.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueNmqVLKE4ml-B_qyVSLWr36LG-8q-9fn9wIsuS3jbbXmsSeDBn3Jw4cpSvXvMLo2GpJg30KcF4tSvrokRSTLqhrOMZya5eBPn3e5LXRiZ2ea7c2tYDTe_evIFQcwHe51Aygn0BlmV-lN90-tMdhC5rvM-ad1QRp67T4fvNHql_i09tViw11bq9-tHHw/s320/boga-21-topraga-gomulen-tohum-albedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikYU5ZouGYTnHIuwU5RMu8BbbHDylBpb3adB2h8nLDmnsrYnN21dvqWdw_2t0jYTdTKNggkA4tKurwNdMnbtQCS8AFyRleq_r_tqXIg_JGw6ao-EwVK4gpeaTd0EJBYcqF11pRPUwK-5lQ0ljBjx5esxFkWlQ4ey3Y9YfSDSQNyKCpsp5fSE5G26FYf4s/s320/boga-22-yeseren-filiz-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVZNt6PiWC7_cWcw1NIF_VluTLh9kJp9UDpOT8tJBzOaoY67Sin3Pfj23SkotvWbp9z7A3J6blfm2VndW7e1HxyFYv_SUZ1C_eFEmsJe1mTlVdzcqYob2Jk07lcxtlHvvchBrqF_pCknP77v1RVbHxl36EKAyX-Y8Ix_E0o3BBLYxZNzav2ZKigjOR7_k/s320/boga-23-isigin-optugu-cicek-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEw-SO0FAoxxKlsAerUQ6y4NLE9CgpKO9Z_QMc4cIy5BEDI8mZZvt6LkJ6ROaaa14U2-LPTXsXHLKb6NRoFjblqYT4MNDdpt6mze2ZN7fXR6qV1YwVKmmXsXnnBvEVo3BS5A4O1ed7LnYUXPPZc7LEZAgM6ERpnK5-UVZ7e-bFZMcWv_YM9o9MDaNX5fA/s320/boga-24-tapinakta-ekmek-paylasimi-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAVtRfReFLgCjlqfLx6rUfro3_VgubTb-7_tvDL6sjXzy1nQv0UvatDMuxLcD52wbk9gwTLjC0i2VNuMxrT3Qy-u7T5BGUgbmK91Sp6WFy7j-QzPV7TlrB3buyXWVYYqQwGLvnojUsF5NV2fkDmefdNvfkbenruWHLQi2PwZshgq0lzvXlJ9P1ROPWrO0/s320/boga-25-inci-denizin-yuzeyine-cikar-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiumHpm2OOG1xPFBDo5msHr_A1I1cIeX71z6S7boFND_2LvKuABO3TPkv_YuDIcovgP2thgmLRYKyWyiVcEapaq6pwTOBVGyYmnvLDfrTUNWIPUmfC2Sdr8XHlaFKrKxJ_UA_P9qNjHNZYlXQZIGvstv1eqHR1ikzEmGlPUgiiC-GUREp4kkrwm0ITtqiw/s320/boga-26-bolluk-tanricasi-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirjYDHwW3IkntZcac1U3MwqVcuse_ppO1XXaHpRpBlWxAG6j57wXjGKi9Xhu20cyKRrK6IWa_3Vg_HaiHB9VVVEj16AUWmXqBq1sbqgYAoUz_mEKOg1KU_H7xN-xIlYu3KlQ78HxMzi_lVwN4mDDCX2O0Cne53DqeOCNuFTGd-WuFgcxfFqsVsp6sELYo/s320/boga-27-bahar-bayrami-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDYorQ-YzVzWRsESQnvilwVQ6-n-a_AlgdInyCNLzS5eXRo_lPAqcwL3T_x22z1JOpnUJCcCfd9qaPzk5x_wQ2SnwS-aKza0ucbnNjnqQLXlRSVNMESceNWIYgYiCf_LnKKMzt-8GF2e1cpl5xpw71mVelOmniS3I5jDhHdjjh8mGFLz_lDw79E6WRre8/s320/boga-28-altin-vazo-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3JRdgDKS1PuBwQ4_bVG9meivcVSDWT510Q5NCRmCGzHZzm-1Oh1KPRX81AKgCRZJdviuOWuhK2_Hj2jzUbpAEjR8-1CjS8RcCnT0hhrMgsvFDgMnIzF2Z4pHWnmipaMobZzwl5nCap2X9P7NsdQDsSioAPs3IIz1TIdzClrcU41bH3gJTlsH2Fm1TiP4/s320/boga-29-gul-bahcesi-rubedo-tabirly.jpeg
https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlLiNWbs9FOn3RsSWkOfLSO9_X-frs-fxJm_RlS1vkfgu27ubOO9pGz2AM5GkxbfjsOqZWbRi8NpWWewjkFfXrE6dg1lSRYxwyLsDnAPm8Vg57dASMHaBRSSIO0ZmYy4BWyrH2G4Bz_-1SBqedyX4NVOaqr50KwRmmqfGyiHSi7OjmgFOHOkfmzkxAPig/s320/boga-30-kutsal-isik-topragi-sarar-rubedo-tabirly.jpeg
"""

new_entries = []
for line in links_text.strip().split("\n"):
    if not line.strip(): continue
    # Extract the identifier, e.g. boga-4 from .../boga-4-yontulmus...
    match = re.search(r'/(boga-\d+)-', line)
    if match:
        key = match.group(1)
        url = line.replace('/s320/', '/w600-rw/')
        new_entries.append(f'            "{key}": "{url}"')

new_content = ",\n".join(new_entries)

with open('c:\\Users\\User\\Desktop\\02_Simulatorler_ve_Ezoterik_Araclar\\Hermetik Astroloji\\build_html.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of imageLinks
content = content.replace('            "koc-30": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9qoHWsCQEt-wDM-wCu_TK5HSDYRwePAV5fWvpaNxpUgH_W4tT4ixOgiyG5MnvUYRVIrcFBHPy4IP-MQtyc4zoV829LLlFKhcTK2-j50MH4kX1oVY1GuXQAfoCb2OefMgSJl9ZJKjH3f4VJ8tonQCUA7z8xNjhUIyFF6BDNz2MxkLn_fzK8VoohJe-iiE/s800/koc-30-altin-bir-isik-halkasi-rubedo.jpeg"\n        };',
                          '            "koc-30": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9qoHWsCQEt-wDM-wCu_TK5HSDYRwePAV5fWvpaNxpUgH_W4tT4ixOgiyG5MnvUYRVIrcFBHPy4IP-MQtyc4zoV829LLlFKhcTK2-j50MH4kX1oVY1GuXQAfoCb2OefMgSJl9ZJKjH3f4VJ8tonQCUA7z8xNjhUIyFF6BDNz2MxkLn_fzK8VoohJe-iiE/s800/koc-30-altin-bir-isik-halkasi-rubedo.jpeg",\n' + new_content + '\n        };')

with open('c:\\Users\\User\\Desktop\\02_Simulatorler_ve_Ezoterik_Araclar\\Hermetik Astroloji\\build_html.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated build_html.py")
