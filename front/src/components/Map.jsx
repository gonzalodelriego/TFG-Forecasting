import React from 'react';
import {
    GoogleMap,
    withScriptjs,
    withGoogleMap
}from 'react-google-maps'

const Map = (props) =>{
    return (
    <GoogleMap
        defaultZoom={9}
        defaultCenter = {{lat : 43.428299, lng: -3.799151}}
    />

    );
};

export default withScriptjs(
    withGoogleMap(
        Map
    )
)