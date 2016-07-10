import {connect} from 'react-redux';
import AreaChart from 'components/AreaTrend/AreaChart';

const mapStateToProps = state => {
    return {
        location: state.searchCondition.location
    }
}

const mapDispatchToProps = dispatch => {
    return {

    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(AreaChart);
