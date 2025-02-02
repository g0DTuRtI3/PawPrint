import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./LandingPage"
import MainPage from "./MainPage";

function App() {

  return (
    <Router>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/view" element={<MainPage />} />
            </Routes>
        </Router>
  );

}

export default App
