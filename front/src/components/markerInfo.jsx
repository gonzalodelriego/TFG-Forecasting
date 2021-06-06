import { useState } from "react";
import InfoWindow from "react-google-maps/lib/components/InfoWindow";
import Marker from "react-google-maps/lib/components/Marker";


const MarkerWithInfoWindow = ({ title, label, position, infoWindowContent }) => {
    const [showInfoWindow, setShowInfoWindow] = useState(false);
    const [clicked, setClicked] = useState(false)

    return (
        <Marker
            title={title}
            label={label}
            position={position}
            onClick={() => {
                setShowInfoWindow(!showInfoWindow);
                setClicked(!clicked);
            }}
        >
            {
                showInfoWindow &&
                <InfoWindow onCloseClick={() => {
                    setShowInfoWindow(false);
                    setClicked(false);
                }}>
                    {infoWindowContent}
                </InfoWindow>
            }
        </Marker>
    );
};

export default MarkerWithInfoWindow;