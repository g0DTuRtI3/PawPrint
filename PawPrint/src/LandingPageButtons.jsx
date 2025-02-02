import { useNavigate } from "react-router-dom";
import './LandingPage.css';


function LandingPageButtons() {

    const navigate = useNavigate();

    const handleLoginClick = () => {
        navigate("/view");  // Redirect to MainPage
    };

    return (
        <div className="buttons-container">
            <button className="Login_btn" style={{ gridRow: "1", gridColumn: "2" }} onClick={handleLoginClick}>Login</button>
            <button className="SignUp_btn" style={{ gridRow: "2", gridColumn: "3" }}>Sign Up</button>
            <button className="QR_btn" style={{ gridRow: "2", gridColumn: "1" }}>QR Code Scan</button>
        </div>
    );
}

export default LandingPageButtons


