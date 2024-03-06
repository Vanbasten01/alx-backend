import createPushNotificationsJobs from "./8-job.js";
const kue = require('kue');
import { expect } from 'chai';

describe('createPushNotificationsJobs', function () {
  let queue;

  // Before running the tests, we set up the queue in test mode
  before(function (done) {
    queue = kue.createQueue();
    queue.testMode.enter();
    done();
  });

  // After running the tests, we clear the queue and exit test mode
  after(function (done) {
    queue.testMode.clear();
    queue.testMode.exit();
    done();
  });

  // Test cases
  it('should throw an error if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create push notification jobs and add them to the queue', function () {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '0987654321', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate the jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
  });
});
