import  React from "react";
import {
  GoogleMap,
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
      <MarkerWithInfoWindow
        title={"Messurement point"}
        label = {"P"}
        position={{
          lat: 44.3171689,
          lng: -4.2709794,
        }}
        infoWindowContent={
          <div>
            <h2>Segunda Playa del Sardinero</h2>
            <img src="https://static.eldiariomontanes.es/www/multimedia/202012/08/media/cortadas/surf-kYiH-U1201000552681BHE-624x385@Diario%20Montanes.jpg" alt = "La imagen no se pudo cargar"></img>
            <h4>Latitud: 44.3171689 Longitud: -4.2709794</h4>
            <h4>Descripción:</h4>
            <p>
              Se ha escogido este punto geográfico ya que se encuentra una 
              de las Boyas del Estado. 
              Se consideró interesante contrastar la información recibida
              de la API, con la captada en tiempo real por la boya.
            </p>
          </div>
        }
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
              La segunda playa del Sardinero  orientada al nordeste,
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
            <h4>Vientos favorables: Oeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo: +2 m</h4>
            <h4>Descripción:</h4>
            <p>
              La primera playa del Sardinero orientada al nordeste,
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
            <h3>Calificación: {spots.somo.toString()}</h3> 
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.459567 Longitud: -3.731702</h4>
            <h4>Vientos favorables: Este, Sureste, Suroeste, Sur</h4>
            <h4>Marea: Baja</h4>
            <h4>Mar de fondo óptimo:  0.8 - 1.8m</h4>
            <h4>Descripción:</h4>
            <p>
              La playa de somo es una de las playas mas largas de la comunidad 
              cántabra. Idónea para principiantes. Su situaicón geográfica, en 
              la puerta de salida de la Bahía de Santander, hace que se formen
              fondos a lo largo de toda la playa. Está bastante expuesta al mar
              de fondo y eso provoca que con condiciones bajas, se pueda disfrutar
              de un día de surfing. 
              Su gran extensión permite que hayan olas "buenas" con muchas direcciones
              de vientos.
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
            <h3>Calificación: {spots.santamarina.toString()}</h3> 
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.46996 Longitud: -3.729709</h4>
            <h4>Vientos favorables: Este, Nordeste, Sureste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo: +1.9m</h4>
            <h4>Descripción:</h4>
            <p>
            Comunmente conocida como "La Isla", La Isla de Santa Marina es uno
            de los puntos más emblemáticos del surfing de olas grandes del norte 
            de España. Su gran exposición a los mares de fondo sumado a la gran 
            profundidad de sus fondos, hacen que sean necesarias unas condiciones
            muy concretas para poder surfear en este lugar.
            Las olas pueden varíar desde un metro de altura hasta los siete metros 
            de altura.
            Es una ola para personas con un nivel más avanzado, que sepan moverse
            bien en el agua y tengan cierta experiencia con olas de mayor tamaño.
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
            <h3>Calificación: {spots.langre.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.476222 Longitud: -3.690878</h4>
            <h4>Vientos favorables: Oeste (flojo), Sureste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  1.5 - 2.5m</h4>
            <h4>Descripción:</h4>
            <p>
            Situada en las cercanías de la Isla de Santa Marina, Langre, es una playa 
            de arena, muy recomendable para la gente que se inicia en el deporte.
            Las olas que rompen en este punto, no son muy fuertes, por lo que 
            suele ser un "spot" al que la gente que surfea frecuentemente no suele acudir.
            Esto es una ventaja para los novatos que quieran más tranquilidad
            en el agua.
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
            <h3>Calificación: {spots.usgo.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.43925 Longitud: -4.000097</h4>
            <h4>Vientos favorables: Oeste (flojo), Sureste, Suroeste, Sur</h4>
            <h4>Marea: Baja</h4>
            <h4>Mar de fondo óptimo:  1.3 - 2m</h4>
            <h4>Descripción:</h4>
            <p>
            La gran desaprovechada, Usgo, es una playa situada al oste de la salida
            de la ría del Pas. Cuenta con una gran exposición al mar de Fondo
            al igual que Canallave y Valdearenas, pero a diferencia de estas, 
            está orientada al nordeste.
            Con un muro de roca natural en su derecha, permite que los vientos que 
            llegan del oeste, sean bloqueados y no perjudiquen a las olas.
            Es una ola a la que suelen ir los más principiantes por su constancia
            en días de olas además de su baja fama y por lo tanto, menor 
            presencia de surfistas.
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
            <h3>Calificación: {spots.brusco.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.469395 Longitud: -3.48325</h4>
            <h4>Vientos favorables: Sureste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta</h4>
            <h4>Mar de fondo óptimo:  1.7 - 4m</h4>
            <h4>Descripción:</h4>
            <p>
            Seguramente, la mejor ola de la Comunidad de Cantabria.
            Una ola potente, para surfistas mucho mas expertos en el deporte.
            Sus fondos arenosos, suelen formar triángulos de arena 
            perfectos que hacen que las olas rompan de una manera "espectacular".
            Combinado con vientos del sur, el Brusco, es la joya para 
            los surfistas a los que les gustan los tubos. 
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
            <h3>Calificación: {spots.fortaleza.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.438774 Longitud: -3.430684</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Baja</h4>
            <h4>Mar de fondo óptimo: +3.4 m</h4>
            <h4>Descripción:</h4>
            <p>
            Seguramente el lugar más bonito para surfear en Cantabria.
            Es una ola que rara vez rompe, debido a la enorme cantidad 
            de factores que se tienen que dar para que hayan olas.
            Situada bajo los acantilados del monte Buciero, pasando las
            ruinas de las fortalezas que Napoleón Bonaparte, junto con
            otros líderes que han conquistado el territorio en el pasado,
            la ola de la Fortaleza es de gran exigencia en cuanto a físico 
            se refiere. 
            Al estar en la salida de la Bahía de Santoña se forman corrientes
            fortísimas en el transcurso de las mareas.
            No es una ola dificil, pero es aconsejable estar en buena forma física.
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
            <h3>Calificación: {spots.laredo.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.43925 Longitud: -4.000097</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  +2m</h4>
            <h4>Descripción:</h4>
            <p>
              Justo al otro lado de la Bahía de Santoña, nos encontramos con
              la playa más larga de Cantabria, la Playa de Laredo.
              Protegida por el monte Buciero y orientada el nordeste, hace de
              esta playa, una alternativa para surfear con condiciones meteorológicas
              similares a las que se tienen que dar para ir a surfear al Sardinero.
              Es una ola para surfistas de todos los niveles. Perfecta para los principiantes
              cuando las condiciones son flojas, y olas muy potentes para 
              surfistas más avanzados cuando se intensifican los vientos y el mar de
              fondo.
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
            <h3>Calificación: {spots.farolillo.toString()}</h3> 
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.393261 Longitud: -4.382461</h4>
            <h4>Vientos favorables: Oeste(flojo), Sureste, Suroeste, Sur</h4>
            <h4>Marea: Medio Baja </h4>
            <h4>Mar de fondo óptimo: 1.8 - 3m</h4>
            <h4>Descripción:</h4>
            <p>
             Al estar situada en la salida del puerto del pueblo de 
             San Vicente de la Barquera, se van acumulando con el flujo de los
             mares y mareas, sedimentos junto al espigón que se encuentra aquí.
             En el espigón hay un faro el cual da nombre a esta ola.
             Una ola para surfistas de todos los niveles. 
             La ola rompe a unos diez metros del farolillo, donde se encuentra
             el fondo de arena. Para llegar a ese punto, es recomendable remar
             pegado al espigón ya que se forman corrientes que impiden que 
             las olas rompan y por ende, sea más fácil desplazarse hasta el punto
             de la rompiente.
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
            <h3>Calificación: {spots.gerra.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.400513 Longitud: -4.361021</h4>
            <h4>Vientos favorables: Este, Nordeste, Suroeste, Sur, Sureste</h4>
            <h4>Marea: Baja</h4>
            <h4>Mar de fondo óptimo:  0.8 - 2m</h4>
            <h4>Descripción:</h4>
            <p>
            En el lado opuesto de la playa de San Vicente de la Barquera,
            encontramos la Playa de Gerra. 
            Es un punto muy expuesto a los vientos del oeste y noroeste,
            así como al mar de fondo de la misma dirección.
            Al ser un fondo de arena, es muy dificil definir la rompiente.
            Es una ola para nivel intermedio, ya que se suelen formar
            grandes corrientes que requieren de conocimiento de la zona.
            El largo camino de acceso hasta la playa, hace de esta un lugar
            único, ya que muchos surfistas evitan ir debido al tiempo que se 
            tarda solo en ir.
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
            <img src="https://lh6.googleusercontent.com/-nK6W0s4UTQ0/VN25YVWrVOI/AAAAAAAAGvc/57xjrQFvpYM/%25252523%25252523%25252526ObssesionSurf%25252Bby%25252B%25252540yleniarc.png" alt = "La imagen no se pudo cargar"></img>
            <h3>Calificación: {spots.canallave.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.452057 Longitud: -3.961576</h4>
            <h4>Vientos favorables: Este, Sureste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  0.5 - 1.8m</h4>
            <h4>Descripción:</h4>
            <p>
            Junto con Valdearenas, es la playa más constante a nivel de 
            olas durante todo el año. 
            De menor extensión que Valdearenas, es un lugar perfecto, para 
            todos los niveles de surfing. 
            Cuando el mar de fondo sube, se forman olas en toda la playa, 
            que, junto con una combinación de buenos vientos, pueden 
            formar olas tuberas. 
            Canallave, es el punto de mayor exposición del norte de España, 
            por lo que normalmente, suelen formarse olas por muy bajo que sea
            el mar de fondo.
            A pesar de su variedad en las olas, es importante conocer el terreno
            ya que al estar en la salida de una ría sumado a la retirada del agua
            de las olas, hace, que se formen corrientes muy fuertes que pueden llevar
            a desgracias.
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
            <h3>Calificación: {spots.valdearenas.toString()}</h3> 
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.447482 Longitud: -3.969581</h4>
            <h4>Vientos favorables: Este, Sureste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  0.5 - 1.8m</h4>
            <h4>Descripción:</h4>
            <p>
            Junto con Canallave, es la playa más constante a nivel de 
            olas durante todo el año. 
            Con una extensión de más de un kilómetro, es un lugar perfecto, para 
            todos los niveles de surfing. 
            Cuando el mar de fondo sube, se forman olas en toda la playa, 
            que, junto con una combinación de buenos vientos, pueden 
            formar olas tuberas. 
            Valdearenas, es el punto de mayor exposición del norte de España, 
            por lo que normalmente, suelen formarse olas por muy bajo que sea
            el mar de fondo.
            A pesar de su variedad en las olas, es importante conocer el terreno
            ya que al estar en la salida de una ría sumado a la retirada del agua
            de las olas, hace, que se formen corrientes muy fuertes que pueden llevar
            a desgracias.
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
            <h3>Calificación: {spots.rosamunda.toString()}</h3>
            <h4>Fondo: Roca </h4>
            <h4>Latitud: 43.484427 Longitud: -3.83373</h4>
            <h4>Vientos favorables: Este, Nordeste, Suroeste, Sur, Sureste</h4>
            <h4>Marea: Medio Alta </h4>
            <h4>Mar de fondo óptimo:  1.3 - 2m</h4>
            <h4>Descripción:</h4>
            <p>
            Entrente de la Playa de Rosamunda, actualmente practicamente
            inexistente, se encuentra un fondo de roca donde rompe una 
            de las olas más emblemáticas de la zona de Santander.
            Protegida por los vientos del este por un saliente, Rosamunda
            es de los puntos más frecuentados debido a su regularidad.
            Es un punto bastante expuesto al mar de fondo, lo que se traduce,
            en menor necesidad de olas grandes para que sea posible surfear ahí.
            Es importante ir con la marea medio alta ya que si está muy baja, el 
            fondo de Roca aparece en la superficie del agua, haciendo muy peligrosa
            la práctica del surf.
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
            <h3>Calificación: {spots.matalenias.toString()}</h3>
            <h4>Fondo: Arena </h4>
            <h4>Latitud: 43.486226 Longitud: -3.787333</h4>
            <h4>Vientos favorables: Oeste, Noroeste, Suroeste, Sur</h4>
            <h4>Marea: Baja</h4>
            <h4>Mar de fondo óptimo:  2m</h4>
            <h4>Descripción:</h4>
            <p>
            Entre Cabo Mayor y Cabo Menor, se encuentra la Playa
            De Mataleñas. 
            Al igual que en el sardinero, para que haya olas en esta
            playa, es necesario que las condiciones meteorológicas sean 
            un poco potentes.
            Normalmente, existen dos rompientes claras, una a la izquierda
            de la playa y otra a la derecha formada por un rebote.
            Es una ola un tanto impredecible porque a pesar de ser para 
            todos los niveles, en función de como esté el fondo de Arena
            ese día, las olas pueden ponerse más fuertes.
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
            <img src="http://2.bp.blogspot.com/-mt6goZTLffo/Vn5vMI_fJVI/AAAAAAAAMI4/80S2R_W0fsc/s1600/12391286_1250548641638652_1950110644071827136_n.jpg" alt = "La imagen no se pudo cargar"></img>
            <h3>Calificación: {spots.caniones.toString()}</h3>
            <h4>Fondo: Roca </h4>
            <h4>Latitud: 43.483348 Longitud: -3.837553</h4>
            <h4>Vientos favorables: Este, Sureste, Suroeste, Sur</h4>
            <h4>Marea: Alta - Medio Alta/Baja - Baja</h4>
            <h4>Mar de fondo óptimo:  1,1 a 2m</h4>
            <h4>Descripción:</h4>
            <p>
            Enfrente del Centro de Interpretación del Litoral "La Maruca",
            las olas rompen en un fondo de roca por lo que no varían.
            Es la mejora ola para los surfistas de un nivel medio bajo.
            Es posible coger olas que van del medio metro a los dos metros y medio.
            Para entrar a la rompiente existen varias maneras
             - Desde el puerto de la Maruca.
             - Saltando desde enfrente de la rompiente.
             - Desde la playa de Rosamunda.
            El gran rango de tamaños de olas que soporta la rompiente, hacen de 
            ésta, una de las olas más versátiles.

            </p>
          </div>
        }
      />
    </GoogleMap>
  );
};

export default withScriptjs(withGoogleMap(Map));
