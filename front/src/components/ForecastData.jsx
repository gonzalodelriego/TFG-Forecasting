import React, {useEffect, useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
//const json_path = require('/Users/G/Desktop/Uneat/Semestre2/TFG/code-repository/TFG-Forecasting/front/src/storage/web.json')


const useStyles = makeStyles({
    table: {
        minWidth: 650,
        maxWidth: 700
    },
});

export default function DenseTable(props) {


    const classes = useStyles();
    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} size="small" aria-label="a dense table">
                <TableHead>
                    <TableRow>
                    {props.webjson.headers.map((row =>
                            <TableCell align ='right'>{row}</TableCell>
                    ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    <TableRow>
                        {props.webjson.swellDirection.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {props.webjson.swellHeight.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {props.webjson.swellPeriod.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {props.webjson.windSpeed.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {props.webjson.windDirection.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {props.webjson.tide.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {props.webjson.waterTemperature.map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                </TableBody>
            </Table>
        </TableContainer>
    );
}
