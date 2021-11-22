import React from 'react'
import "./Header.css"
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { IconButton } from '@mui/material';
import RefreshIcon from '@mui/icons-material/Refresh';

function Header(){
    return (
        <div className="header"> 
            <IconButton> <AccountCircleIcon className="iconos__header" fontSize="large" /> </IconButton>
            <h1>MusicR</h1>
            <IconButton> <RefreshIcon className="iconos__header" fontSize="large" /> </IconButton>
        </div>

    );


}

export default Header;