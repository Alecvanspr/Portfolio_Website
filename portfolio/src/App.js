import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CVScene from './CV/CVScene';
import HomeScene from './Home/HomeScene';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomeScene />} />
        <Route path="/cv" element={<CVScene/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
