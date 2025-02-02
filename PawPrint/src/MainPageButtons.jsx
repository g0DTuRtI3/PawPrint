import './MainPage.css';

function MainPageButtons({ onEditClick }) {

    return (
        <div className="buttons-container-mainPage">
            <button className="editBtn" onClick={onEditClick}>Edit</button>
        </div>
    );
}

export default MainPageButtons;
