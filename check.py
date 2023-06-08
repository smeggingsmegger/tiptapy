#!/usr/bin/env python3

import tiptapy

def main():
    s = '''{
        "type" : "doc",
        "content" : [
            {
                "type" : "heading",
                "attrs" : {
                    "id" : "AUDQP34ROnuHiJ7EWAyQp",
                    "textAlign" : "left",
                    "level" : 1
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "TESTING THIS 1"
                    }
                ]
            },
            {
                "type" : "heading",
                "attrs" : {
                    "id" : "PQVuyGR97f2D-ChMmkRbl",
                    "textAlign" : "left",
                    "level" : 2
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "TESTING THIS 2"
                    }
                ]
            },
            {
                "type" : "heading",
                "attrs" : {
                    "id" : "vuQ4O96retuMLONFEf4Uj",
                    "textAlign" : "left",
                    "level" : 3
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "Testing This 3"
                    }
                ]
            },
            {
                "type" : "heading",
                "attrs" : {
                    "id" : "Owr6yfCfY8Uqc3sQI26F8",
                    "textAlign" : "left",
                    "level" : 4
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "Testing this 4"
                    }
                ]
            },
            {
                "type" : "heading",
                "attrs" : {
                    "id" : "Ne3c9h-1mIAmqT_4BpZSg",
                    "textAlign" : "left",
                    "level" : 5
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "Testing this 5"
                    }
                ]
            },
            {
                "type" : "heading",
                "attrs" : {
                    "id" : "gvxETx5RVczR5QrViMUby",
                    "textAlign" : "left",
                    "level" : 6
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "Testing This 6"
                    }
                ]
            },
            {
                "type" : "paragraph",
                "attrs" : {
                    "id" : "h2wPs1ZaYQUcFmLFy4kHl",
                    "blockWidth" : "normal",
                    "textAlign" : "left"
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "This is a "
                    },
                    {
                        "type" : "text",
                        "marks" : [
                            {
                                "type" : "bold"
                            }
                        ],
                        "text" : "paragraph"
                    },
                    {
                        "type" : "text",
                        "text" : " "
                    },
                    {
                        "type" : "text",
                        "marks" : [
                            {
                                "type" : "italic"
                            }
                        ],
                        "text" : "of"
                    },
                    {
                        "type" : "text",
                        "text" : " "
                    },
                    {
                        "type" : "text",
                        "marks" : [
                            {
                                "type" : "code",
                                "attrs" : {
                                    "id" : null
                                }
                            }
                        ],
                        "text" : "text"
                    },
                    {
                        "type" : "text",
                        "text" : ". It's "
                    },
                    {
                        "type" : "text",
                        "marks" : [
                            {
                                "type" : "strike"
                            }
                        ],
                        "text" : "pretty"
                    },
                    {
                        "type" : "text",
                        "text" : " "
                    },
                    {
                        "type" : "text",
                        "marks" : [
                            {
                                "type" : "highlight"
                            }
                        ],
                        "text" : "dope"
                    },
                    {
                        "type" : "text",
                        "text" : ". Blah blah blah."
                    }
                ]
            },
            {
                "type" : "bulletList",
                "attrs" : {
                    "id" : "I7CxT7i48ix3IWGne1Jm4"
                },
                "content" : [
                    {
                        "type" : "listItem",
                        "attrs" : {
                            "id" : "OeG4Kt4CliurrRI0eg6Ak"
                        },
                        "content" : [
                            {
                                "type" : "paragraph",
                                "attrs" : {
                                    "id" : "isxvWVuTt8NbjnSetfmzI",
                                    "blockWidth" : "normal",
                                    "textAlign" : "left"
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Testing"
                                    }
                                ]
                            },
                            {
                                "type" : "bulletList",
                                "attrs" : {
                                    "id" : "_vBY2toSjaaXwh2XWNQAh"
                                },
                                "content" : [
                                    {
                                        "type" : "listItem",
                                        "attrs" : {
                                            "id" : "7EeJjk6iYmGkdXZl8rVYj"
                                        },
                                        "content" : [
                                            {
                                                "type" : "paragraph",
                                                "attrs" : {
                                                    "id" : "Cz63OVE3N22_4lSNkLVUI",
                                                    "blockWidth" : "normal",
                                                    "textAlign" : "left"
                                                },
                                                "content" : [
                                                    {
                                                        "type" : "text",
                                                        "text" : "Test"
                                                    }
                                                ]
                                            },
                                            {
                                                "type" : "bulletList",
                                                "attrs" : {
                                                    "id" : "Khxhki-YRfHTxoq0XuCE0"
                                                },
                                                "content" : [
                                                    {
                                                        "type" : "listItem",
                                                        "attrs" : {
                                                            "id" : "bBzrGPus6NO_4FfaI3QST"
                                                        },
                                                        "content" : [
                                                            {
                                                                "type" : "paragraph",
                                                                "attrs" : {
                                                                    "id" : "FKey7YIh9C86JFy8Q_JcL",
                                                                    "blockWidth" : "normal",
                                                                    "textAlign" : "left"
                                                                },
                                                                "content" : [
                                                                    {
                                                                        "type" : "text",
                                                                        "text" : "Testing!"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "type" : "taskList",
                "attrs" : {
                    "id" : "vjoJ5q76vvpHtGobHZ5DH"
                },
                "content" : [
                    {
                        "type" : "taskItem",
                        "attrs" : {
                            "id" : "VwZYer14kIvVo_TD_6Uel",
                            "checked" : false
                        },
                        "content" : [
                            {
                                "type" : "paragraph",
                                "attrs" : {
                                    "id" : "gRaRNa5WvSFdwTeIDZ4s4",
                                    "blockWidth" : "normal",
                                    "textAlign" : "left"
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "One Task"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type" : "taskItem",
                        "attrs" : {
                            "id" : "Rr1k8v8iFwOLz97ut49a1",
                            "checked" : false
                        },
                        "content" : [
                            {
                                "type" : "paragraph",
                                "attrs" : {
                                    "id" : "dZFPR7lERezzSjA12kyiv",
                                    "blockWidth" : "normal",
                                    "textAlign" : "left"
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Two Task"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type" : "taskItem",
                        "attrs" : {
                            "id" : "0KFElZoa06EGECUFhC3T0",
                            "checked" : false
                        },
                        "content" : [
                            {
                                "type" : "paragraph",
                                "attrs" : {
                                    "id" : "ZpC9U1TBZDsLdCJNr8hSc",
                                    "blockWidth" : "normal",
                                    "textAlign" : "left"
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Red Task"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type" : "taskItem",
                        "attrs" : {
                            "id" : "P4n1t8FGldiAXOLKRs_rU",
                            "checked" : false
                        },
                        "content" : [
                            {
                                "type" : "paragraph",
                                "attrs" : {
                                    "id" : "3G749vr6dQ48aBjYlIAH4",
                                    "blockWidth" : "normal",
                                    "textAlign" : "left"
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Blue Task"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "type" : "blockquote",
                "attrs" : {
                    "blockWidth" : "normal"
                },
                "content" : [
                    {
                        "type" : "paragraph",
                        "attrs" : {
                            "id" : "qmiBwNrA3ToF4fH3EFMkL",
                            "blockWidth" : "normal",
                            "textAlign" : "left"
                        },
                        "content" : [
                            {
                                "type" : "text",
                                "text" : "Testing this quote!"
                            }
                        ]
                    }
                ]
            },
            {
                "type" : "orderedList",
                "attrs" : {
                    "id" : "j73c17JJy3hYGzOpC_Lz_",
                    "start" : 1
                },
                "content" : [
                    {
                        "type" : "listItem",
                        "attrs" : {
                            "id" : "mQzN4XO0_r26uYxTI-FLb"
                        },
                        "content" : [
                            {
                                "type" : "paragraph",
                                "attrs" : {
                                    "id" : "hlGrinE1WLGuT5EPCANrm",
                                    "blockWidth" : "normal",
                                    "textAlign" : "left"
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Testing"
                                    }
                                ]
                            },
                            {
                                "type" : "orderedList",
                                "attrs" : {
                                    "id" : "qC4CqdzwYw3zBS2pf5kqO",
                                    "start" : 1
                                },
                                "content" : [
                                    {
                                        "type" : "listItem",
                                        "attrs" : {
                                            "id" : "BMs8MibnA9u5rbKdRdA2C"
                                        },
                                        "content" : [
                                            {
                                                "type" : "paragraph",
                                                "attrs" : {
                                                    "id" : "C1zQSnAMCg_B89z61X_Od",
                                                    "blockWidth" : "normal",
                                                    "textAlign" : "left"
                                                },
                                                "content" : [
                                                    {
                                                        "type" : "text",
                                                        "text" : "Test"
                                                    }
                                                ]
                                            },
                                            {
                                                "type" : "orderedList",
                                                "attrs" : {
                                                    "id" : "pbzI0c4sgHOM_dzT-lsj0",
                                                    "start" : 1
                                                },
                                                "content" : [
                                                    {
                                                        "type" : "listItem",
                                                        "attrs" : {
                                                            "id" : "bpMRUteN0Nn81Tl77_Lll"
                                                        },
                                                        "content" : [
                                                            {
                                                                "type" : "paragraph",
                                                                "attrs" : {
                                                                    "id" : "PzRaaBxWpOvSxnVakcPut",
                                                                    "blockWidth" : "normal",
                                                                    "textAlign" : "left"
                                                                },
                                                                "content" : [
                                                                    {
                                                                        "type" : "text",
                                                                        "text" : "Testing!"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "type" : "image",
                "attrs" : {
                    "id" : "VWtaui4kuBMte4xyd7asd",
                    "src" : "https://files-dev.lokcrm.com/carefully-crafted/irW_Ymvh0b.jpeg",
                    "alt" : null,
                    "title" : null
                }
            },
            {
                "type" : "codeBlock",
                "attrs" : {
                    "language" : null
                },
                "content" : [
                    {
                        "type" : "text",
                        "text" : "from python import superior"
                    }
                ]
            },
            {
                "type" : "horizontalRule",
                "attrs" : {
                    "blockWidth" : "normal"
                }
            },
            {
                "type" : "table",
                "content" : [
                    {
                        "type" : "tableRow",
                        "content" : [
                            {
                                "type" : "tableHeader",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Testing"
                                    }
                                ]
                            },
                            {
                                "type" : "tableHeader",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Testing 2"
                                    }
                                ]
                            },
                            {
                                "type" : "tableHeader",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "Testing 3"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type" : "tableRow",
                        "content" : [
                            {
                                "type" : "tableCell",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "1"
                                    }
                                ]
                            },
                            {
                                "type" : "tableCell",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "2"
                                    }
                                ]
                            },
                            {
                                "type" : "tableCell",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "3"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type" : "tableRow",
                        "content" : [
                            {
                                "type" : "tableCell",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "1"
                                    }
                                ]
                            },
                            {
                                "type" : "tableCell",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "2"
                                    }
                                ]
                            },
                            {
                                "type" : "tableCell",
                                "attrs" : {
                                    "colspan" : 1,
                                    "rowspan" : 1,
                                    "colwidth" : null
                                },
                                "content" : [
                                    {
                                        "type" : "text",
                                        "text" : "3"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "type" : "popItem",
                "attrs" : {
                    "id" : "WcAk3th0xh_kVZGTnU9qU",
                    "heading" : "Client Contacts",
                    "text" : "The primary client contacts for this project are as follows:",
                    "kind" : "Contacts"
                }
            },
            {
                "type" : "signature",
                "attrs" : {
                    "id" : "Px34hGXQeZhBBaiE1Ox5a",
                    "contact_id" : null,
                    "signatureDetails" : {
                        
                    },
                    "email" : "",
                    "title" : "",
                    "locked" : false,
                    "contact_details" : {
                        
                    },
                    "contact_org_details" : {
                        
                    },
                    "signature_request_id" : null,
                    "signed_on" : null,
                    "secure_hash" : null
                }
            },
            {
                "type" : "paragraph",
                "attrs" : {
                    "id" : "n_fESvNvy8w6uv5ofR5fc",
                    "blockWidth" : "normal",
                    "textAlign" : "left"
                }
            }
        ]
    }'''

    class config:
        """
        Config class to store constants used by the other nodes.
        """
        DOMAIN = "python.org"


    renderer = tiptapy.BaseDoc(config)
    out = renderer.render(s)
    print(out)


if __name__ == '__main__':
    main()