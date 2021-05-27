import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from "axios";
import credentials from "/Users/G/Desktop/Uneat/Semestre2/TFG/code-repository/TFG-Forecasting/front/src/credentials.js";

 const json_path = require('/Users/G/Desktop/Uneat/Semestre2/TFG/code-repository/TFG-Forecasting/front/src/storage/web.json')

// async function getData() {
//     let res = await axios.get(`${credentials.cloud_function}`);
//     const data = res.data;
//     console.log(data);
// }
//
// const json_path = getData();

const useStyles = makeStyles({
    table: {
        minWidth: 650,
        maxWidth: 700
    },
});

export default function DenseTable() {
    const classes = useStyles();

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} size="small" aria-label="a dense table">
                <TableHead>
                    <TableRow>
                    {json_path['headers'].map((row =>
                            <TableCell align ='right'>{row}</TableCell>
                    ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    <TableRow>
                        {json_path['swellDirection'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {json_path['swellHeight'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {json_path['swellPeriod'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {json_path['windSpeed'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {json_path['windDirection'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {json_path['tide'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                    <TableRow>
                        {json_path['waterTemperature'].map((row =>
                                <TableCell align ='right'>{row}</TableCell>
                        ))}
                    </TableRow>
                </TableBody>
            </Table>
        </TableContainer>
    );
}
