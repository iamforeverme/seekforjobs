import SearchBox from 'components/SearchBox';
import {changeKeyword, changeLocation, changePeriod} from 'actions';
import {connect} from 'react-redux';


const mapStateToProps = state => {
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
      }
  }
}


export default connect(
    mapStateToProps,
    mapDispatchToProps
)(SearchBox);
