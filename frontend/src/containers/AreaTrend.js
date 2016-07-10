import {connect} from 'react-redux';
import AreaTrend from 'components/AreaTrend';

const mapStateToProps = state => {
    console.log("yangyang state", state);
    return {
        jobData: state.area.job,
        incomeData: state.area.income
    }
}

const mapDispatchToProps = dispatch => {
    return {

    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(AreaTrend);
