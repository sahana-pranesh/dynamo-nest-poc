import { ChartRequest } from 'src/dto/chart.request';

export const generateHash = (request: ChartRequest): string => {
    const crypto = require('crypto');
    var hash = crypto.getHashes();
    var value = request.ID + request.display + request.location;
    for (var keyword in request.keywords) {
        value = value + keyword
    }
    var hashPwd = crypto.createHash('sha1').update(value).digest('hex');

    console.log("Hashed pwd", hashPwd);
    return hashPwd;
}
