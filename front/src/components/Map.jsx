import React from 'react';
import {
    GoogleMap,
    Marker,
    withScriptjs,
    withGoogleMap
}from 'react-google-maps'
const json_path = require('/Users/G/Desktop/Uneat/Semestre2/TFG/code-repository/TFG-Forecasting/front/src/storage/web.json')
const Map = (props) =>{
    return (
        <GoogleMap
            defaultZoom={10}
            defaultCenter = {{lat : 43.428299, lng: -3.799151}}
        >
            {/*SEGUNDA_SARDINERO*/}
            <Marker
                title = {'Segunda'}
                label = {json_path['calification'][0]['sardinero_dos']}
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
                position={{
                    lat: 43.473578,
                    lng: -3.781434
                }}
            />
            {/*SOMO*/}
            <Marker
                position={{
                    lat: 43.459567,
                    lng: -3.731702
                }}
            />
            {/*ISLA DE SANTAMARINA*/}
            <Marker
                position={{
                    lat: 43.469960,
                    lng: -3.729709
                }}
            />
            {/*LANGRE*/}
            <Marker
                position={{
                    lat: 43.475341,
                    lng: -3.729709
                }}
            />
            {/*USGO*/}
            <Marker
                position={{
                    lat: 43.439250,
                    lng: -4.000097
                }}
            />
            {/*BRUSCO*/}
            <Marker
                position={{
                    lat: 43.469395,
                    lng: -3.483250
                }}
            />
            {/*FORTALEZA*/}
            <Marker
                position={{
                    lat: 43.438774,
                    lng: -3.430684
                }}
            />
            {/*LAREDO*/}
            <Marker
                position={{
                    lat: 43.416957,
                    lng: -3.434862
                }}
            />
            {/*FAROLILLO*/}
            <Marker
                position={{
                    lat: 43.393261,
                    lng: -4.382461
                }}
            />
            {/*GERRA*/}
            <Marker
                position={{
                    lat: 43.400513,
                    lng: -4.361021
                }}
            />
            {/*CANALLAVE*/}
            <Marker
                position={{
                    lat: 43.452057,
                    lng: -3.961576
                }}
            />
            {/*VALDEARENAS*/}
            <Marker
                position={{
                    lat: 43.447482,
                    lng: -3.969581
                }}
            />
            {/*VALDEARENAS*/}
            <Marker
                position={{
                    lat: 43.447482,
                    lng: -3.969581
                }}
            />
            {/*ROSAMUNDA*/}
            <Marker
                position={{
                    lat: 43.484427,
                    lng: -3.833730
                }}
            />
            {/*MATALEÑAS*/}
            <Marker
                position={{
                    lat: 43.486226,
                    lng: -3.787333
                }}
            />
            {/*CAÑONES*/}
            <Marker
                position={{
                    lat: 43.483348,
                    lng: -3.837553
                }}
            />


            {/*            <Marker>
                position= {{lat: 43.477236, lng: -3.786591}} />
            </Marker>*/}


        </GoogleMap>


    );
};

export default withScriptjs(
    withGoogleMap(
        Map
    )
)