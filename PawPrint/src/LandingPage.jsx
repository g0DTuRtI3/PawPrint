import LandingPageTitle from "./LandingPageTitle"
import LandingPageButtons from "./LandingPageButtons";
import './LandingPage.css';
import LandingPageImages from "./LandingPageImages";

function LandingPage() {
    return (
        <>
            <LandingPageTitle/>
            <div className="wrapper">
                <div className="rectangle1">
                    <LandingPageImages/>
                    <LandingPageButtons/>
                </div>
            </div>
        </>
    );

}

export default LandingPage


