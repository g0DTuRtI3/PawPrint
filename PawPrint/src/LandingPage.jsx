import LandingPageTitle from "./LandingPageTitle"
import LandingPageButtons from "./LandingPageButtons";
import LandingPageImages from "./LandingPageImages";
import './LandingPage.css';

function LandingPage() {
    return (
        <>
            <LandingPageTitle/>
            <div className="wrapper">
                <div className="rectangleBorder">
                    <LandingPageImages/>
                    <LandingPageButtons/>
                </div>
            </div>
        </>
    );

}

export default LandingPage


