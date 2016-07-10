import EmploymentChart from 'components/AreaTrend/EmploymentChart';
import {connect} from 'react-redux';

const mapStateToProps = state => {
    console.log("yangyang state", state);
    return {
        jobData: state.area.job
    }
}

const mapDispatchToProps = dispatch => {
    return {

    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(EmploymentChart);
