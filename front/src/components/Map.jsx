import React from "react";
import {
  GoogleMap,
  Marker,
  withScriptjs,
  withGoogleMap,
} from "react-google-maps";

import MarkerWithInfoWindow from './markerInfo';

const Map = (props) => {
  const arrayspots = props.webjson.calification;
  const spots = arrayspots[0];

  return (
    <GoogleMap
      defaultZoom={10}
      defaultCenter={{ lat: 43.428299, lng: -3.799151 }}
    >
      {/*PUNTO DE MEDICIÓN*/}
      <Marker
        title={"Messurement point"}
        label={"P"}
        position={{
          lat: 44.3171689,
          lng: -4.2709794,
        }}
      />

      {/*SEGUNDA_SARDINERO*/}
      <MarkerWithInfoWindow
        title={"Segunda"}
        label = {spots.sardinero_dos.toString()}
        position={{
          lat: 43.477236,
          lng: -3.786591,
        }}
        infoWindowContent={
          <div>
            <h2>Segunda Playa del Sardinero</h2>
            <img src="https://static.eldiariomontanes.es/www/multimedia/202012/08/media/cortadas/surf-kYiH-U1201000552681BHE-624x385@Diario%20Montanes.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.477236 Longitud: -3.786591</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo: +2 m</h4>
            <h4>Descripción:</h4>
            <p>
              La segunda playa del Sardinero está orientada al nordeste,
              protegida por cabo Mayor y cabo Menor, hace de ésta, un lugar
              idóneo cuando las condicones meteorológicas son más "fuertes". La
              baja exposición hacia el mar de fondo, tiene como resultante que
              sea necesario que grandes mares lleguen a sus costas, para poder
              ver alguna ola "surfeable". El fondo de la segunda, es plano, por
              lo que no hay una rompiente clara donde las olas rompan siempre.
              Se extiende desde el Chiqui, hasta Piquío, teniendo un gran número
              de lugares donde poder surfear. Perfecta para principiantes si las
              condiciones no son muy potentes.
          </p>
          </div>
        }
      />

      {/*PRIMERA_SARDINERO*/}
      <MarkerWithInfoWindow
        title={"Primera"}
        label={spots.sardinero_uno.toString()}
        position={{
          lat: 43.473578,
          lng: -3.781434,
        }}
        infoWindowContent={
          <div>
            <h2>Primera Playa del Sardinero</h2>
            <img src="https://www.escueladesurfmolinucos.com/wp-content/uploads/sb-instagram-feed-images/153700014_138446584815527_3897118128072265375_nfull.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.473578 Longitud: -3.781434</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo: +2 m</h4>
            <h4>Descripción:</h4>
            <p>
              La segunda playa del Sardinero está orientada al nordeste,
              protegida por cabo Mayor y cabo Menor, hace de ésta, un lugar
              idóneo cuando las condicones meteorológicas son más "fuertes". La
              baja exposición hacia el mar de fondo, tiene como resultante que
              sea necesario que grandes mares lleguen a sus costas, para poder
              ver alguna ola "surfeable". El fondo de la segunda, es plano, por
              lo que no hay una rompiente clara donde las olas rompan siempre.
              Se extiende desde el Chiqui, hasta Piquío, teniendo un gran número
              de lugares donde poder surfear. Perfecta para principiantes si las
              condiciones no son muy potentes.
            </p>
          </div>
        }
      />
      {/*SOMO*/}
      <MarkerWithInfoWindow
        title={"Somo"}
        label={spots.somo.toString()}
        position={{
          lat: 43.459567,
          lng: -3.731702,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Somo</h2>
            <img src="https://i0.wp.com/www.todosurf.com/wp-content/uploads/2019/08/Playas-de-Somo-y-Loredo-1.jpeg?fit=1280%2C551&ssl=1" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.459567 Longitud: -3.731702</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*ISLA DE SANTAMARINA*/}
      <MarkerWithInfoWindow
        title={"Isla"}
        label={spots.santamarina.toString()}
        position={{
          lat: 43.46996,
          lng: -3.729709,
        }}
        infoWindowContent={
          <div>
            <h2>Isla de Santamarina</h2>
            <img src="https://surfnaturealliance.org/wp-content/uploads/2015/01/PR-SANTAMARINA.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.46996 Longitud: -3.729709</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*LANGRE*/}
      <MarkerWithInfoWindow
        title={"Langre"}
        label={spots.langre.toString()}
        position={{
          lat: 43.476222,
          lng: -3.690878,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Langre</h2>
            <img src="https://ec2-im-1.msw.ms/md/image.php?id=386887&type=PHOTOLAB&resize_type=STREAM_MEDIUM_SQUARE&fromS3" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.476222 Longitud: -3.690878</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*USGO*/}
      <MarkerWithInfoWindow
        title={"Playa de Usgo"}
        label={spots.usgo.toString()}
        position={{
          lat: 43.43925,
          lng: -4.000097,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Usgo</h2>
            <img src="http://4.bp.blogspot.com/-B5TAgpNNxyA/T3Dn3FfzCzI/AAAAAAAAAD8/842DsT4G3J8/s1600/CSC_0591.JPG" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.43925 Longitud: -4.000097</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />

      {/*BRUSCO*/}
      <MarkerWithInfoWindow
        title={"Playa del Brusco"}
        label={spots.brusco.toString()}
        position={{
          lat: 43.469395,
          lng: -3.48325,
        }}
        infoWindowContent={
          <div>
            <h2>Playa del Brusco</h2>
            <img src="https://www.surf-forecast.com/system/images/16617/large/El-Brusco.jpg?1470292805" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.469395 Longitud: -3.48325</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*FORTALEZA*/}
      <MarkerWithInfoWindow
        title={"Fortaleza de Napoleón"}
        label={spots.fortaleza.toString()}
        position={{
          lat: 43.438774,
          lng: -3.430684,
        }}
        infoWindowContent={
          <div>
            <h2>Fortaleza de Napoleón Bonaparte</h2>
            <img src="https://www.surfmarket.org/media/com_mtree/images/listings/m/1745.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.438774 Longitud: -3.430684</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*LAREDO*/}
      <MarkerWithInfoWindow
        title={"Playa de Laredo"}
        label={spots.laredo.toString()}
        position={{
          lat: 43.416957,
          lng: -3.434862,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Laredo</h2>
            <img src="https://www.singlequiver.com/enelpico/wp-content/uploads/2018/09/29744736_10211397644284433_2960710722623373962_o.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.43925 Longitud: -4.000097</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>
            </p>
          </div>
        }
      />
      {/*FAROLILLO*/}
      <MarkerWithInfoWindow
        title={"Playa de San Vicente"}
        label={spots.farolillo.toString()}
        position={{
          lat: 43.393261,
          lng: -4.382461,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de San Vicente de la Barquera</h2>
            <img src="https://www.singlequiver.com/enelpico/wp-content/uploads/2016/06/photo_2018-08-21_14-30-33.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.393261 Longitud: -4.382461</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*GERRA*/}
      <MarkerWithInfoWindow
        title={"Playa de Gerra"}
        label={spots.gerra.toString()}
        position={{
          lat: 43.400513,
          lng: -4.361021,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Gerra</h2>
            <img src="https://ec2-im-1.msw.ms/md/image.php?id=361381&type=PHOTOLAB&resize_type=STREAM_MEDIUM_SQUARE&fromS3" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.400513 Longitud: -4.361021</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*CANALLAVE*/}
      <MarkerWithInfoWindow
        title={"Playa de Canallave"}
        label={spots.canallave.toString()}
        position={{
          lat: 43.452057,
          lng: -3.961576,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Canallave</h2>
            <img src="https://static.eldiariomontanes.es/www/multimedia/202012/08/media/cortadas/surf-kYiH-U1201000552681BHE-624x385@Diario%20Montanes.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.452057 Longitud: -3.961576</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*VALDEARENAS*/}
      <MarkerWithInfoWindow
        title={"Playa de Valdearenas"}
        label={spots.valdearenas.toString()}
        position={{
          lat: 43.447482,
          lng: -3.969581,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Valdearenas</h2>
            <img src="https://surflimitmagazine.com/wp-content/uploads/2020/08/SL-20080409548.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.447482 Longitud: -3.969581</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*ROSAMUNDA*/}
      <MarkerWithInfoWindow
        title={"Playa de Rosamunda"}
        label={spots.rosamunda.toString()}
        position={{
          lat: 43.484427,
          lng: -3.83373,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Rosamunda</h2>
            <img src="https://static1.hoy.es/www/pre2017/multimedia/RC/201308/21/viajes/Media/cantabria-santa-marina--253x140.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.484427 Longitud: -3.83373</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />

      {/*MATALEÑAS*/}
      <MarkerWithInfoWindow
        title={"Playa de Mataleñas"}
        label={spots.matalenias.toString()}
        position={{
          lat: 43.486226,
          lng: -3.787333,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de Mataleñas</h2>
            <img src="https://www.surfsearchspot.com/wp-content/uploads/2016/07/surfear-en-berria-2.png" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.486226 Longitud: -3.787333</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
      {/*Cañones*/}
      <MarkerWithInfoWindow
        title={"Playa de Cañones"}
        label={spots.caniones.toString()}
        position={{
          lat: 43.483348,
          lng: -3.837553,
        }}
        infoWindowContent={
          <div>
            <h2>Playa de La Maruca - Cañones</h2>
            <img src="https://static.eldiariomontanes.es/www/multimedia/202012/08/media/cortadas/surf-kYiH-U1201000552681BHE-624x385@Diario%20Montanes.jpg" alt = "La imagen no se pudo cargar"></img>
            {/* <h3>Calificación: {spots.sardinero_dos.toString()}</h3> */}
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.483348 Longitud: -3.837553</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  m</h4>
            <h4>Descripción:</h4>
            <p>

            </p>
          </div>
        }
      />
    </GoogleMap>
  );
};

export default withScriptjs(withGoogleMap(Map));
