import './LandingPage.css';

function LandingPageButtons() {
    return (
        <div className="buttons-container">
            <button className="Login_btn" style={{ gridRow: "1", gridColumn: "2" }}>Login</button>
            <button className="SignUp_btn" style={{ gridRow: "2", gridColumn: "3" }}>Sign Up</button>
            <button className="QR_btn" style={{ gridRow: "2", gridColumn: "1" }}>QR Code Scan</button>
        </div>
    );
}

export default LandingPageButtons


