import React from "react";
import Button from '@mui/material/Button';
import { createTheme } from '@mui/material/styles';
import { ThemeProvider } from "@emotion/react";
import { Grid, Typography } from "@mui/material";

const URL_AUTH = "https://accounts.spotify.com/authorize?client_id=c176bd9d61984d3f8c4804b03245467a&response_type=code&redirect_uri=http://localhost:3000/redirect&scope=streaming%20user-read-private%20user-library-read%20user-library-modify%20user-modify-playback-state"

const theme = createTheme({
    palette: {
      primary: {
        // Purple and green play nicely together.
        main: '#1db954',
        contrastText: '#ffffff'
      },
    },
  });

export default function Login(){
    return(
        <div>
          <Grid container justify="center" alignItems="center" direction="column" style={{ height:"100vh" }}>
            <Grid item>
              <Typography align="center" style={{height:"100vh"}}>
                <ThemeProvider theme={theme}>
                  <Button variant="contained" href={URL_AUTH} color="primary">Inicia sesion a Spotify</Button>
                </ThemeProvider>
              </Typography>
            </Grid>
          </Grid>
        </div>

    )
}

