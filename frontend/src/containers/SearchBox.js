import SearchBox from 'components/SearchBox';
import {changeKeyword, changeLocation, changePeriod, queryJob, updateJobData} from 'actions';
import {connect} from 'react-redux';
import {browserHistory} from 'react-router';


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
      },
      searchHandler: () => {
         dispatch(queryJob());
         //dispatch(updateJobData({'week':0}))
         browserHistory.push("/area");
      }
  }
}


export default connect(
    mapStateToProps,
    mapDispatchToProps
)(SearchBox);
