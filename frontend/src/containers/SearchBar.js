import SearchBar from 'components/SearchBar';
import {connect} from 'react-redux';

const mapStateToProps = (state) => {
    console.log("yangyang, search bar state", state)
    return {
        keyword: state.searchCondition.keyword,
        location: state.searchCondition.location,
        period: state.searchCondition.period
    }
}

export default connect(
    mapStateToProps
)(SearchBar);
