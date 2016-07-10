import SearchBar from 'components/SearchBar';
import {connect} from 'react-redux';
import {changeKeyword, changeLocation, changePeriod} from 'actions';

const mapStateToProps = (state) => {
    console.log("yangyang, search bar state", state)
    return {
        keyword: state.searchCondition.keyword,
        location: state.searchCondition.location,
        period: state.searchCondition.period
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
      changeHandler: (field, state)=>{
          switch (field) {
              case 'keyword':
                  dispatch(changeKeyword(state));
                  break;
              case 'location':
                  dispatch(changeLocation(state));
                  break;
              case 'period':
                  dispatch(changePeriod(state));
                  break;
              default:
                  return;
          }
      },
      searchHandler: () => {

      }
  }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(SearchBar);
