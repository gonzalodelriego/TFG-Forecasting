import React from 'react';
import {
    GoogleMap,
    Marker,
    withScriptjs,
    withGoogleMap
}from 'react-google-maps'
//const json_path = require('/Users/G/Desktop/Uneat/Semestre2/TFG/code-repository/TFG-Forecasting/front/src/storage/web.json')
const Map = (props) =>{
    const arrayspots = props.webjson.calification
    const spots = arrayspots[0]
    return (

        <GoogleMap
            defaultZoom={10}
            defaultCenter = {{lat : 43.428299, lng: -3.799151}}
        >

            {/*PUNTO DE MEDICIÓN*/}
            <Marker
                title = {'Messurement point'}
                label = {'P'}
                position={{
                    lat: 44.3171689,
                    lng: -4.2709794
                }}
            />
            {/*SEGUNDA_SARDINERO*/}
            <Marker
                title = {'Segunda'}
                label = {spots.sardinero_dos.toString()}
                position={{
                    lat: 43.477236,
                    lng: -3.786591
                }}
                icon={{
                    url:'/Users/G/Desktop/Uneat/Semestre2/TFG/code-repository/TFG-Forecasting/front/src/icons/ocean32x32.png',
                    anchor: (32,32),
                    scaledSize: (64,64)}}
            />
            {/*PRIMERA_SARDINERO*/}
            <Marker
                title = {'Primera'}
                label = {spots.sardinero_uno.toString()}
                position={{
                    lat: 43.473578,
                    lng: -3.781434
                }}
            />
            {/*SOMO*/}
            <Marker
                title = {'Somo'}
                label = {spots.somo.toString()}
                position={{
                    lat: 43.459567,
                    lng: -3.731702
                }}
            />
            {/*ISLA DE SANTAMARINA*/}
            <Marker
                title = {'Isla'}
                label = {spots.santamarina.toString()}
                position={{
                    lat: 43.469960,
                    lng: -3.729709
                }}
            />
            {/*LANGRE*/}
            <Marker
                title = {'Langre'}
                label = {spots.langre.toString()}
                position={{
                    lat: 43.475341,
                    lng: -3.729709
                }}
            />
            {/*USGO*/}
            <Marker
                title = {'Usgo'}
                label = {spots.usgo.toString()}
                position={{
                    lat: 43.439250,
                    lng: -4.000097
                }}
            />
            {/*BRUSCO*/}
            <Marker
                title = {'Brusco'}
                label = {spots.brusco.toString()}
                position={{
                    lat: 43.469395,
                    lng: -3.483250
                }}
            />
            {/*FORTALEZA*/}
            <Marker
                title = {'Fortaleza'}
                label = {spots.fortaleza.toString()}
                position={{
                    lat: 43.438774,
                    lng: -3.430684
                }}
            />
            {/*LAREDO*/}
            <Marker
                title = {'Laredo'}
                label = {spots.laredo.toString()}
                position={{
                    lat: 43.416957,
                    lng: -3.434862
                }}
            />
            {/*FAROLILLO*/}
            <Marker
                title = {'Farolillo'}
                label = {spots.farolillo.toString()}
                position={{
                    lat: 43.393261,
                    lng: -4.382461
                }}
            />
            {/*GERRA*/}
            <Marker
                title = {'Gerra'}
                label = {spots.gerra.toString()}
                position={{
                    lat: 43.400513,
                    lng: -4.361021
                }}
            />
            {/*CANALLAVE*/}
            <Marker
                title = {'Canallave'}
                label = {spots.canallave.toString()}
                position={{
                    lat: 43.452057,
                    lng: -3.961576
                }}
            />
            {/*VALDEARENAS*/}
            <Marker
                title = {'Valdearenas'}
                label = {spots.valdearenas.toString()}
                position={{
                    lat: 43.447482,
                    lng: -3.969581
                }}
            />
            {/*ROSAMUNDA*/}
            <Marker
                title = {'Rosamunda'}
                label = {spots.rosamunda.toString()}
                position={{
                    lat: 43.484427,
                    lng: -3.833730
                }}
            />
            {/*MATALEÑAS*/}
            <Marker
                title = {'Mataleñas'}
                label = {spots.caniones.toString()}
                position={{
                    lat: 43.486226,
                    lng: -3.787333
                }}
            />
            {/*CAÑONES*/}
            <Marker
                title = {'Cañones'}
                label = {spots.caniones.toString()}
                position={{
                    lat: 43.483348,
                    lng: -3.837553
                }}
            />
        </GoogleMap>


    );
};

export default withScriptjs(
    withGoogleMap(
        Map
    )
)