import './App.css';
import Login from './Login';
import Interfaz from './Interfaz';

const code = new URLSearchParams(window.location.search).get('code');

function App() {
  return code ? <Interfaz code={code} /> : <Login />;
}

export default App;
