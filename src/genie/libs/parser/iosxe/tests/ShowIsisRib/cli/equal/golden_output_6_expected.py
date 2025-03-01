expected_output = {
    "tag": {
        "1": {
            "prefix": {
                "4.4.4.4": {
                    "subnet": "32",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": False,
                        "n_flag": True
                    },
                    "source_router_id": "4.4.4.4",
                    "prefix_sid_index": 4,
                    "via_interface": {
                        "MPLS-SR-Tunnel6": {
                            "distance": 115,
                            "route_type": "L1",
                            "metric": 70,
                            "via_ip": "6.6.6.6",
                            "src_ip": "4.4.4.4",
                            "tag": "0",
                            "host": "R3.00-00",
                            "lsp": {
                                "next_hop_lsp_index": 3,
                                "rtp_lsp_index": 4,
                                "rtp_lsp_version": 0,
                                "tpl_lsp_version": 52
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "src_router_id": "4.4.4.4",
                            "label": "16004",
                            "u_loop_enabled": True
                        },
                        "Ethernet1/2": {
                            "distance": 115,
                            "route_type": "L1",
                            "metric": 70,
                            "via_ip": "20.20.10.2",
                            "src_ip": "4.4.4.4",
                            "tag": "0",
                            "host": "R3.00-00",
                            "lsp": {
                                "next_hop_lsp_index": 3,
                                "rtp_lsp_index": 4,
                                "rtp_lsp_version": 52,
                                "tpl_lsp_version": 52
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "src_router_id": "4.4.4.4",
                            "label": "16004",
                            "repair_path": {
                                "ip": "5.5.5.5",
                                "interface": "MPLS-SR-Tunnel4",
                                "metric": 65,
                                "attributes": {
                                    "DS": True,
                                    "LC": False,
                                    "NP": False,
                                    "PP": False,
                                    "SR": True
                                },
                                "next_hop_ip": "10.10.20.2",
                                "next_hop_interface": "Ethernet1/1",
                                "lfa_type": "TI-LFA link-protecting",
                                "label": "16003",
                                "nodes": {
                                    "host": {
                                        "R4": {
                                            "node_type": "P",
                                            "ip": "4.4.4.4",
                                            "label": "16004"
                                        },
                                        "R5": {
                                            "node_type": "P",
                                            "ip": "5.5.5.5",
                                            "label": "16005"
                                        }
                                    }
                                }
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "prefix_sid_index": 3,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "repair_source": {
                                "host": "R3",
                                "rtp_lsp_index": 3
                            }
                        }
                    }
                }
            }
        }
    }
}