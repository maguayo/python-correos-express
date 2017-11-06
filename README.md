Correos express
===


Usage Examples
--------------

    import correosexpress
    correos = correosexpress.Picking('USERNAME', 'PASSWORD')
    correos.create({
        "solicitante": "SOLICITANTE_PASSWORD",
        "canalEntrada": "",
        "numEnvio": "",
        "ref": "GrabEnvioEOFEtiqueta",
        "refCliente": "",
        "fecha": "31102017",
        "codRte": "600000017",
        "nomRte": "PRUEBA EOF2",
        "nifRte": "",
        "dirRte": "C/NUEVA, 2",
        "pobRte": "MADRID",
        "codPosNacRte": "28010",
        "paisISORte": "",
        "codPosIntRte": "",
        "contacRte": "",
        "telefRte": "",
        "emailRte": "",
        "codDest": "",
        "nomDest": "PRUEBAEOF",
        "nifDest": "",
        "dirDest": "TEST, 22",
        "pobDest": "MADRID",
        "codPosNacDest": "28010",
        "paisISODest": "",
        "codPosIntDest": "",
        "contacDest": "NOMBRE DESTINO",
        "telefDest": "600000000",
        "emailDest": "",
        "contacOtrs": "",
        "telefOtrs": "",
        "emailOtrs": "",
        "observac": "ninguna",
        "numBultos": "1",
        "kilos": "1",
        "volumen": "",
        "alto": "",
        "largo": "",
        "ancho": "",
        "producto": "63",
        "portes": "P",
        "reembolso": "",
        "entrSabado": "",
        "seguro": "",
        "numEnvioVuelta": "",
        "listaBultos": [{
            "alto": "",
            "ancho": "",
            "codBultoCli": "",
            "codUnico": "",
            "descripcion": "",
            "kilos": "",
            "largo": "",
            "observaciones": "",
            "orden": "1",
            "referencia": "",
            "volumen": ""
        }],
        "codDirecDestino": "2828194",
        "password": "",
        "listaInformacionAdicional": [{
            "tipoEtiqueta": "2",
        }]
    })

    # Create and Save the label for printing
    correos.save_label("/home/project_name/media/label1.pdf")


TODO:
--------

- Track order

