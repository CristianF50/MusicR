import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {BrowserRouter} from 'react-router-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { SnackbarProvider } from 'notistack';
import Fade from '@material-ui/core/Fade';

ReactDOM.render(
  <SnackbarProvider maxSnack={3} anchorOrigin={{
    vertical: 'bottom',
    horizontal: 'center',
}}
TransitionComponent={Fade}>
    <App />
</SnackbarProvider>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
