import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles({
    table: {
        minWidth: 650,
        maxWidth: 700
    },
});

function createData(param, sheight, speriod, sdirection, wspeed,wdir) {
    return { param, sheight, speriod, sdirection, wspeed,wdir };
}
function getData(json){
    const datos = JSON.parse(json);
    for(let dia = 0; dia<datos.length - 1;dia++){
        for(let hora = 0;hora<datos[dia].length;hora++){
            var obj = datos[dia][hora];
            console.log(obj.swellDirection)
        }
    }
}
const rows = [
    createData('Wind Speed', 159, 6.0, 24, 4.0),
    createData('Wind Direction', 237, 9.0, 37, 4.3),
    createData('Wave (m)', 262, 16.0, 24, 6.0),
    createData('Period', 305, 3.7, 67, 4.3),
    createData('Swell Direction', 356, 16.0, 49, 3.9),
    createData('Tide', 356, 16.0, 49, 3.9),
    createData('Water Temperature', 356, 16.0, 49, 3.9),
];

export default function DenseTable() {
    const classes = useStyles();

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} size="small" aria-label="a dense table">
                <TableHead>
                    <TableRow>
                        <TableCell>Params</TableCell>
                        <TableCell align="right">L.2 05h</TableCell>
                        <TableCell align="right">L.2 10h</TableCell>
                        <TableCell align="right">L.2 15h</TableCell>
                        <TableCell align="right">L.2 20h</TableCell>
                        <TableCell align="right">L.2 23h</TableCell>
                        <TableCell align="right">M.3 05h</TableCell>
                        <TableCell align="right">M.3 10h</TableCell>
                        <TableCell align="right">M.3 15h</TableCell>
                        <TableCell align="right">M.3 20h</TableCell>
                        <TableCell align="right">M.3 23h</TableCell>
                        <TableCell align="right">X.4 05h</TableCell>
                        <TableCell align="right">X.4 10h</TableCell>
                        <TableCell align="right">X.4 15h</TableCell>
                        <TableCell align="right">X.4 20h</TableCell>
                        <TableCell align="right">X.4 23h</TableCell>
                        <TableCell align="right">J.5 05h</TableCell>
                        <TableCell align="right">J.5 10h</TableCell>
                        <TableCell align="right">J.5 15h</TableCell>
                        <TableCell align="right">J.5 20h</TableCell>
                        <TableCell align="right">J.5 23h</TableCell>
                        <TableCell align="right">V.6 05h</TableCell>
                        <TableCell align="right">V.6 10h</TableCell>
                        <TableCell align="right">V.6 15h</TableCell>
                        <TableCell align="right">V.6 20h</TableCell>
                        <TableCell align="right">V.6 23h</TableCell>
                        <TableCell align="right">S.7 05h</TableCell>
                        <TableCell align="right">S.7 10h</TableCell>
                        <TableCell align="right">S.7 15h</TableCell>
                        <TableCell align="right">S.7 20h</TableCell>
                        <TableCell align="right">S.7 23h</TableCell>
                        <TableCell align="right">D.8 05h</TableCell>
                        <TableCell align="right">D.8 10h</TableCell>
                        <TableCell align="right">D.8 15h</TableCell>
                        <TableCell align="right">D.8 20h</TableCell>
                        <TableCell align="right">D.8 23h</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row) => (
                        <TableRow key={row.param}>
                            <TableCell component="th" scope="row">
                                {row.param}
                            </TableCell>
                            <TableCell align="right">{row.sheight}</TableCell>
                            <TableCell align="right">{row.speriod}</TableCell>
                            <TableCell align="right">{row.sdirection}</TableCell>
                            <TableCell align="right">{row.wspeed}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}
