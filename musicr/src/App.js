import './App.css';
import Header from './Header';
import Login from './Login';
import Interfaz from './Interfaz';
import { Routes, Route, Link } from "react-router-dom";

const code = new URLSearchParams(window.location.search).get('code');

function App() {
  return code ? <Interfaz code={code} /> : <Login />;
}

export default App;
