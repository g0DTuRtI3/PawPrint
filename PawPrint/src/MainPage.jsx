import MainPageTables from './MainPageTables';
import './MainPage.css';
import MainPageImages from './MainPageImages';
import MainPageButtons from './MainPageButtons';

function MainPage() {
    return (
        <div className="wrapper">
                <div className="rectangleBorder">
                    <MainPageTables></MainPageTables>
                    <MainPageImages></MainPageImages>
                    <MainPageButtons></MainPageButtons>
                </div>
        </div>
    );
}

export default MainPage;
